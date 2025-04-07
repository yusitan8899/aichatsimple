import requests

def get_github_repo(owner, repo):
    """
    获取GitHub仓库的基本信息
    :param owner: 仓库所有者用户名
    :param repo: 仓库名称
    :return: 仓库信息的字典
    """
    url = f"https://api.github.com/repos/{owner}/{repo}"
    response = requests.get(url)
    
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error: {response.status_code}")
        return None

# 示例：获取requests库的信息
repo_info = get_github_repo("yusitan8899", "aichatsimple")
if repo_info:
    print(f"仓库名: {repo_info['name']}")
    print(f"描述: {repo_info['description']}")
    print(f"星标数: {repo_info['stargazers_count']}")
    print(f"仓库URL: {repo_info['html_url']}")