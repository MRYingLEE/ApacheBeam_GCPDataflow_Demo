
#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
def processOneMsg(element):
    pass

import apache_beam as beam

class OneRowParDo(beam.DoFn):
    def process(self, element):
      return processOneMsg(element)

streamingMode=True #
pubSubTopic="projects/grasshopper-298307/topics/L3toL1"

def run_pipeline():
    if streamingMode:
        options = PipelineOptions(args, save_main_session=True, streaming=True)
    else:
        options = beam.options.pipeline_options.PipelineOptions(streaming=False)
    p = beam.Pipeline(options=options)

    if streamingMode:
      read = (
          p 
          | 'Read from PubSub '>> beam.io.ReadFromPubSub(topic=pubSubTopic)
      )
    else:
      read = (
          p 
          | 'Reads from csv' >> beam.io.ReadFromText('market_data_v2.csv') 
      )
    process= (
        read 
        | 'Structures data' >> beam.ParDo(OneRowParDo())
        | 'Save L1 data into a file' >> beam.io.WriteToText('L1_market_data',file_name_suffix=".csv")
    )
    
    result = p.run()
    result.wait_until_finish()  # For it to hold the terminal until it finishes

run_pipeline()