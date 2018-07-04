# aws-serverless

![webapi](https://raw.githubusercontent.com/anelhaman/aws-serverless/master/screen.png)

## aws see config credentials

```
aws configure
```

## install serverless

```
npm install -g serverless
```

See more [serverless](https://www.npmjs.com/package/serverless) 


## install plugins

```
sls plugin install -n serverless-python-requirements
```

## deploy

```
serverless deploy
```

or

```
sls deploy
```

## try to call

```
sls invoke -f hello
```

or

```
sls invoke -f httprequest
```

### api

after deployed will return

```
endpoints:
 GET - https://XXXXXXXXXX.execute-api.us-east-1.amazonaws.com/dev
```

