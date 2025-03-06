from github import Github
import argparse

# Replace with your GitHub personal access token
TOKEN = '$REPLACE_YOUR_GITHUB_TOKEN'

def find_requirements_files(org_name):
    g = Github(TOKEN)
    org = g.get_organization(org_name)

    requirements_files = []

    for repo in org.get_repos():
        for content in repo.get_contents(""):
            if content.name == "requirements.txt":
                requirements_files.append((repo.full_name, content.html_url))

    return requirements_files

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Find requirements.txt files in a GitHub organization.')
    parser.add_argument('organization', type=str, help='The name of the GitHub organization to search.')
    args = parser.parse_args()

    org_name = args.organization
    requirements_files = find_requirements_files(org_name)

    for repo_name, file_url in requirements_files:
        print(f"Repository: {repo_name}")
        print(f"Requirements.txt URL: {file_url}\n")