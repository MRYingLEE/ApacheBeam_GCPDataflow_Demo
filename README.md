# ApacheBeam_GCPDataflow_Demo
This batch and streaming data processing demo is tested on GCP Dataflow, a Apache Beam Environment.

This demo is intendedly to show the procedure of a Apache Beam Developing instead of specific data processing logic. Actually the code was digested from a busines project. So that the core processing logic has been intendedly deleted in order to avoid business information leak.

# Why Beam? Beam=Batch+strEAM

Apache Beam (https://beam.apache.org/): An advanced unified programming model

Implement batch and streaming data processing jobs that run on any execution engine.

Apache Beam supports distributed processing back-ends, which include Apache Flink, Apache Spark, and Google Cloud Dataflow.

So that Apache Beam application can be deployed on Google Cloud Dataflow as a SERVERLESS solution.

Also, Apache Beam batch application can work in Colab.


# Step 1: Imperative code to process data
Apache Beam is a kind of functional processing platform. So it is hard to debug Beam code.
I suggest to start with an imperative code. And it is easy to use Jupyter Notebook to start if you choose Python as a working lanuage.

# Step 2: Batch code to process data
You may use Jupyter notebook to develop Beam application. 
For small data set, a direct runner of Beam is good enough.


# Step 3: Streaming code to process data
The batch and streaming implementations are all based on Apache Beam and share nearly the same code.

But it is hard to setup a streaming environment. Luckily GCP dataflow has a 
