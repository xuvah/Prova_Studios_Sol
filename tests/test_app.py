import pytest
import random
from app.apiStudiosSol import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_verify_mutation(client):
    placares = [(3, 15), (6, 9), (7, 21),(0, 0)]  # Testando placares factíveis
    print("testando placares factíveis")
    for score1, score2 in placares:
        mutation = f'''
        mutation {{
            verify(score: "{score1}x{score2}") {{
                combinations
            }}
        }}
        '''
        print(f"Score: {score1}x{score2}")
        response = client.post('/graphql', json={'query': mutation})
        json_data = response.get_json()
        resposta=json_data['data']['verify']['combinations']

        print(f"resposta obtida: {resposta}")
        assert 'errors' not in json_data
        assert resposta > 0

def test_verify_mutation_random(client):
    for _ in range(10):  # Teste com 10 placares randômicos (pode gerar placares infactíveis)
        print("testando placares randômicos...")
        score1 = random.randint(0, 30)
        score2 = random.randint(0, 30)
        mutation = f'''
        mutation {{
            verify(score: "{score1}x{score2}") {{
                combinations
            }}
        }}
        '''
        print(f"Score: {score1}x{score2}")
        response = client.post('/graphql', json={'query': mutation})
        json_data = response.get_json()
        resposta=json_data['data']['verify']['combinations']
        print(f"resposta obtida: {resposta}")
        assert 'errors' not in json_data
       
