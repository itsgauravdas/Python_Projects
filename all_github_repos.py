import requests 
import sys 
from github import Github 

github_client=Github()
# username=sys.argv[1]


# url=f"https://api.github.com/users/{username}"

# user_data = requests.get(url).json()


def repository_names(user):
    """Fetches a list of repository objects for a user."""
    repo_names = []
    for repo in user.get_repos():
        repo_names.append(repo)
    return repo_names


def repository_details(user):
    """Fetches detailed information for all repositories of a user."""
    all_repo_details = []
    repo_names = repository_names(user)
    for repo in repo_names:
        repo_details = {
        'Name' : repo.full_name.split("/")[1],
        "Description" : repo.description,
        "Created on" : repo.created_at,
        "Programming language" : repo.language,
        "Forked" : str(repo.forks) + "times(s)"
        }
        all_repo_details.append(repo_details)
    return all_repo_details



if __name__ == '__main__':
    username=input("Enter the Github username :: ")
    
    try:
        user = github_client.get_user(username)
        repo_details = repository_details(user)
        for content in repo_details:
            for title,description in content.items():
                print(title, ":", description)
            print("\n-------------------------------------------------")
    except Exception as e:
        print(f"An error occur {e}")