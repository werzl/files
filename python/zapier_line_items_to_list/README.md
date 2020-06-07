# Zapier Line Items to List

This py script was used as in a Lambda function kicked off from a Zapier automated flow.

When Zapier triggers a Lambda function directly (i.e using an AWS integration instead of API Gateway), the payload isn't sent as normal JSON, like you would expect from making a request to a REST API. Instead, if you have Arrays in your payload, each item is extracted as a long string of comma separated values. This meant I had to translate those comma separated values back into an Array when handling the payload. Being too lazy to switch over to API Gateway, this is what I came up with.

### Prerequisites
Written for Python 3.6 but should work for 3.7.

### Usage
#### input_object
The dictionary from Zapier with comma separated values in place of Arrays.

#### params
A string array with each key in the dictionary to be translated from CSV's -> Array

#### output_object=[]
The Array of extracted values.