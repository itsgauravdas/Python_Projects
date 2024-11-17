from bs4 import BeautifulSoup
import requests
import json 

class   AskUbuntu:
    """
    Create an instance of AskUbuntu class.
    
    python
    question = AskUbuntu("Topic")
    """
    def __init__(self, topic):
        self.topic = topic
    def getQuestion(self):
        
        """
        Class - `AskUbuntu`
        Example:
        ```
        que = AskUbuntu("github")
        scrape = que.getQuestions()
        ```
        Returns:
        {
            "question": question title
            "views": view count of question
            "vote_count": vote count of question
            "answer_count": no. of answers to the question
            "description": description of the question
        }
        """
        url = "https://askubuntu.com/questions/tagged/" + self.topic
        headers = {"User-Agent": "Mozilla/5.0"}
        try:
            """
            
                In BeautifulSoup, both select() and select_one() are methods used to find elements in an HTML document using CSS selectors, but they have different behaviors:select():
                Returns a list of all elements that match the given CSS selector(s).
                Even if only one element matches the selector, it will still return it as a list with that single element.
            """
            res=requests.get(url,headers=headers)
            soup= BeautifulSoup(res.content, 'html.parser')
            
            questions_data ={"question" : []}
            questions = soup.select(".s-post-summary")
            for que in questions:
                title=que.select_one(".s-link").getText()
                """in BeautifulSoup, the .getText() (or .text) method is used to extract the text content from"""
                status = que.select(".s-post-summary--stats-item-number")
                vote = status[0].getText()
                ans=status[1].getText()
                views=status[2].getText()
                
                desc = (
                    que.select_one(".s-post-summary--content-excerpt")
                    .getText()
                    .strip()
                    .encode("ascii","ignore")
                    .decode()
                )
                questions_data["question"].append(
                    {
                        "question" : title,
                        "Views" : views,
                        "Vote_Count" : vote,
                        "answer_count": ans,
                        "Description"  :desc 
                    }
                )
            json_data=json.dumps(questions_data)
            with open('output.json', 'w') as file:
                data=file.write(json_data)
                print('File has been created successfully')
            return json_data 
        
        except ValueError:
            error_message ={
                "message": "No question related to the topic found"
            }   
            ejson=json.dumps(error_message)
            return ejson
        

obj=AskUbuntu("Python")
print(obj.getQuestion())