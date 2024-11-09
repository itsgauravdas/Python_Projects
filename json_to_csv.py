import pandas as pd 
import json
import os 
import oracledb


def json_csv():
    data=pd.read_json('example_2.json')

    q=data['quiz'][0]['q1']['question']
    q1=data['quiz'][1]['q1']['question']

    df=pd.DataFrame({'question_1':[q],'question_2':[q1]})
    df.to_csv('Final.csv',index=False)
    print(f"CSV saved at {os.getcwd()}")
    


def insert_data():
    df=pd.read_csv('Final.csv')
    connection=oracledb.connect(
        user="hr",
        password="hr",
        dsn="localhost/ORCLPDB"
    )
    cursor=connection.cursor()
    for _,i in df.iterrows():
        cursor.execute('INSERT INTO QUESTION (question1,question2) VALUES (:1,:2)',(i['question_1'],i['question_2']))
        
    connection.commit()
    cursor.close()
    connection.close()
    
if __name__ == '__main__':
    
    data=json_csv()
    print('Successfully converted')
    
    insert_data()
    print('Data Inserted successfully')
    
    
