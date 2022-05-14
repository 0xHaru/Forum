from bs4 import BeautifulSoup
from requests import get, post
from requests.exceptions import ConnectionError

addr = "localhost"
port = 8000

def test_profile():
    
    username = "cozis"
    response = get(f"http://{addr}:{port}/users/{username}")
    assert response.status_code == 200
    assert response.headers['Content-Type'] == 'text/html; charset=utf-8'

    data = response.content
    soup = BeautifulSoup(data, 'html.parser')

    # Make sure in at least one <span> 
    # element the username occurres.
    found_username = False
    for span in soup.find_all("span"):
        text = span.get_text()        
        if text == username:
            found_username = True

    assert found_username

if __name__ == "__main__":
    
    tests = [test_profile]

    passed = 0
    
    for no, test in enumerate(tests):
        try:
            test()
            print(f"Test {no}: Passed")
            passed += 1
        except ConnectionError:
            print('Failed to connect! Are you sure the server is up and running?')
            exit(-1)                
        except:
            print(f"Test {no}: Failed")

    total = len(tests)
    print(f'Total: {total}, Passed: {passed}, Failed: {total-passed}')