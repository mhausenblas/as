# as - the acronym solver
These days we have to deal with an ever-growing bunch of acronyms in the ICT domain. I can't always remember all of them and where they have been defined, originally. But I can code. Thus, I coded up `as` the acronym solver, a simple tool that allows you to look-up acronyms. For example:

	input:    BASE
	output:
	          full title: 'basically available, soft state, eventually consistent'
	          reference: http://queue.acm.org/detail.cfm?id=1394128
	
## Usage

Once you have to:

	chmod 755 launch-as.sh
	
and then just launch it:

	./launch-as.sh
	
... and whenever you like you point your browser to `http://localhost:6969/` and should see something like the following:

![Screen-shot of the as](https://github.com/mhausenblas/as/raw/master/doc/as-screenshot.png "Screen-shot of the as")

## Fill the data store

There is no fancy way to get data into the CouchDB implemented here. I assume a CSV file locally (see `as-input.csv`) that is imported into CouchDB like so:

	./launch-as.sh create

... which in turn uses another Python script to read the CSV and create one-by-one CouchDB documents for each row in the CSV. It creates the database if it's not there, no problem, but in order to get the search functionality you need to manually enable indexing on the database (see `https://cloudant.com/#!/dashboard/{account}/{database}/search`).

## License
Public domain.