# aws_bucket_pipeline
Using Python, numpy, pandas, AWS-S3-buckets, boto3, sklearn. I created a pipeline that takes stock data and then processes it, then sends the cleaned data to my AWS S3 bucket for storage.

I take in the Date,Open,High,Low,Close,Volume of a fake stock (right now yfinance is down so I couldn't take real stock data.) 

I'm using MinMaxScaler to scale all data except Date and Volume so that they can be more reasonably compared and I could have an easier time with converting to using any ML/deep learning techniques while it's in a consumable format.

I used a log function on the volume to scale it down heavily as they often can be in the millions and above.
