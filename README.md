# ApacheBeam_GCPDataflow_Demo
This batch and streaming data processing demo is tested on GCP Dataflow, a Apache Beam Environment.

This demo is intendedly to show the procedure of a Apache Beam Developing instead of specific data processing logic. Actually the code was digested from a real project. So that the core processing logic has been intendedly deleted in order to avoid business information leak.

# Why Beam? Beam=Batch+strEAM

Apache Beam (https://beam.apache.org/): An advanced unified programming model

Implement batch and streaming data processing jobs that run on any execution engine.

Apache Beam supports distributed processing back-ends, which include Apache Flink, Apache Spark, and Google Cloud Dataflow.

So that Apache Beam application can be deployed on Google Cloud Dataflow as a SERVERLESS solution.

Also, Apache Beam batch application can work in Colab.


# Step 1: Imperative code to process data
Apache Beam is a kind of functional processing platform. So it is hard to debug Beam code.
I suggest to start with an imperative code. And it is easy to use Jupyter Notebook to start if you choose Python as a working lanuage.

# Step 2: Batch implementation
In order to provide a **Serverless** solution, this task was completed as a notebook. 
This notebook was developed and tested on Colab (https://colab.research.google.com/) along with an Apache Beam DirectRunner.

 <font color=red>Colab will raise some errors for the Apache beam installation. Please ignore them, which won't affect the following functions.</font> 
 
# Step 3: Streaming Implementation

The same code in an independent file, Streaming.py, can be run in streaming mode. The code supports Google PubSub as streaming source.

The streaming implementation is tested on Google Cloud Dataflow platform.

The Google cloud environment will cost a few dollars.

## The Beam environment 

The Beam environment can be set up by following this tutorial (https://console.cloud.google.com/getting-started?walkthrough_tutorial_id=python_dataflow_quickstart&_ga=2.25278013.1291490325.1607857566-321077206.1587778923 )

## The streaming source
The stream source can be simulated by a Google Dataflow template, Text Files on Cloud Storage to Pub/Sub (Stream) (https://cloud.google.com/dataflow/docs/guides/templates/provided-streaming#gcstexttocloudpubsubstream ) 

# Things to consider

## How would you deal with data which arrive out of order?

So far, the implement code only considers basic fault tolerance, such as bid/ask size cannot be negative, even an order size could be negative in the situation of outing of order.

For serious situation of outing of order, the data can be recorded and replyed. In order to save cost, the history can be replayed PER order.

In the streaming mode, some source, such as Google PubSub, can be polled to replay the history.

## Architecture
Due to the shared order book in the memory, the implementation is not scalable. 

Even a STATEFUL Apache Beam doesn't provide the scalability.

In order to be scalable, the shared order book should be put into an external persistent data base, such as Google BigTable.

It depends on the business requirement. If one node can deal with the data in time and the history can be quickly replayed to rebuid the order book. One node model can be accepted. 
