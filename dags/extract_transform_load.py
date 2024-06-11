from airflow import DAG
from airflow.decorators import task
import pandas as pd
import requests
import include.utils as utils

with DAG(
    dag_id="etl_pokemon",
    start_date=datetime(2024, 1, 1),
    schedule="*/5 * * * *",
    catchup=False,
    doc_md=__doc__,
    default_args={"owner": "Astro", "retries": 1}
):
    @task
    def extract_pokemons(**context):
        """
        This task retrieves the 151 1st generation pokemons from wikipedia using pandas.
        """
        pokes_html = pd.read_html(
            "https://https://sv.wikipedia.org/wiki/Lista_över_Pokémon")[1][:151]
        pokemons = {id: name for (id, name) in zip(pokes_html['Nationellt Pokédex'],
                                                    pokes_html['Engelskt namn'])}
        return pokemons
    
    @task
    def transform_load_pokemons(pokemons):
        utils.clear_pokebelt()
        for pokemon in utils.load_catch(pokemons):
            pokemon_json = requests.get(f"https://pokeapi.co/api/v2/pokemon-species/{pokemon.lower()}").json()
            utils.save_pokemon(pokemon_json)

    @task
    def print_pokemon():
        for pokemon in utils.load_pokemons():
            print(f"Pokemon: {pokemon['name']} has base happiness of {pokemon['base_happiness']}")

    transform_load_pokemons(extract_pokemons()) >> print_pokemon()
        