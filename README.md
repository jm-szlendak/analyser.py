A simple app that will analyze the Stack Exchange Data dumps ( https://archive.org/details/stackexchange )

Its able to analyse a massive multi-GB files with small memory footprint. 

Made to play aroud & learn python

Usage: 

```
docker build -t analyser .    
docker run -it -p 5001:5001 analyser    
```

Then:

POST http://localhost:5001/analyse

with XML file to upload. Currently only Posts files are supported.


TODO:
- error handling of malformed inputs
- auto-recognize the kind of data
- support providing the URL to file instead of file itself