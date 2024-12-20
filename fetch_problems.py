import requests

def fetch_problems():
    url = "https://leetcode.com/graphql"
    query = """
    {
        problemsetQuestionList(
            categorySlug: ""
            limit: 10
            skip: 0
            filters: {}
        ) {
            questions {
                title
                titleSlug
                difficulty
                content
            }
        }
    }
    """
    headers = {
        "Content-Type": "application/json",
        "Referer": "https://leetcode.com/problems/"
    }
    response = requests.post(url, json={'query': query}, headers=headers)
    if response.status_code == 200:
        return response.json()['data']['problemsetQuestionList']['questions']
    else:
        raise Exception(f"Query failed to run by returning code of {response.status_code}. {response.text}")

problems = fetch_problems()
for problem in problems:
    print(f"Title: {problem['title']}")
    print(f"Difficulty: {problem['difficulty']}")
    print(f"Content: {problem['content'][:200]}...") 
    print()

