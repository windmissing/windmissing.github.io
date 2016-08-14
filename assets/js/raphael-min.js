<div id="diagram">Diagram will be placed here</div>
<script src="flowchart.js"></script>
<script>
  var diagram = flowchart.parse('st=>start: Start:>http://www.google.com[blank]\n' +
                                'e=>end:>http://www.google.com\n' +
                                'op1=>operation: My Operation\n' +
                                'sub1=>subroutine: My Subroutine\n' +
                                'cond=>condition: Yes \n' +
                                'or No?\n:>http://www.google.com' +
                                'io=>inputoutput|request: catch something...\n' +
                                '' +
                                'st->op1->cond\n' +
                                'cond(yes)->io->e\n' + // conditions can also be redirected like cond(yes, bottom) or cond(yes, right)
                                'cond(no)->sub1(right)->op1');// the other symbols too...
  diagram.drawSVG('diagram');

  // you can also try to pass options:

  diagram.drawSVG('diagram', {
                                'x': 0,
                                'y': 0,
                                'line-width': 3,
                                'line-length': 50,
                                'text-margin': 10,
                                'font-size': 14,
                                'font-color': 'black',
                                'line-color': 'black',
                                'element-color': 'black',
                                'fill': 'white',
                                'yes-text': 'yes',
                                'no-text': 'no',
                                'arrow-end': 'block',
                                'scale': 1,
                                // style symbol types
                                'symbols': {
                                    'start': {
                                      'font-color': 'red',
                                      'element-color': 'green',
                                      'fill': 'yellow'
                                    },
                                    'end':{
                                        'class': 'end-element'
                                    }
                                },
                                // even flowstate support ;-)
                                'flowstate' : {
                                    // 'past' : { 'fill' : '#CCCCCC', 'font-size' : 12},
                                    // 'current' : {'fill' : 'yellow', 'font-color' : 'red', 'font-weight' : 'bold'},
                                    // 'future' : { 'fill' : '#FFFF99'},
                                    'request' : { 'fill' : 'blue'}//,
                                    // 'invalid': {'fill' : '#444444'},
                                    // 'approved' : { 'fill' : '#58C4A3', 'font-size' : 12, 'yes-text' : 'APPROVED', 'no-text' : 'n/a' },
                                    // 'rejected' : { 'fill' : '#C45879', 'font-size' : 12, 'yes-text' : 'n/a', 'no-text' : 'REJECTED' }
                                  }
                              });
</script>
