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


## License
Public domain.