from urllib import response
import boto3
import json

s3 = boto3.client('s3')
def lambda_handler(event,context):
    #lambda collects values from event
    bucket=  event['Records'][0]['s3']['bucket']['name']
    key = event['Records'][0]['s3']['object']['key']
    response= s3.get_object(Bucket=bucket,Key=key)
    content = response['Body']
    jsonload = json.loads(content.read())
    transactions = jsonload['transactions']
    refund_tran=[]
    for transaction in transactions:
        if transaction['transactionType']=='REFUND':
            print("transactiontype:" + transaction['transactionType'])
            print("transactionamount:" + str(transaction['amount']))
            refund_tran.append(transaction)
            
    if len(refund_tran)>=1:
        print("returning refund transation")
        return refund_tran
    else:
        print("No refund transaction")
        return None
    
    

