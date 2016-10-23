({
	//Initial data
	data:{
		sort:"Age ↓", search:"Airplane crash", range:[], result:[]
	},

	require:[{
		"this.List":{
			url:"../testdata/rockstar-deaths.json", dataType:"json"
		}
	}],

	// Inits form
	init: function ($form, form){
		var that = this,
				d = form.data,
				list;
		// Build HTML
		$form
		.html(that.HTML.join(""))
		.on("click", "x", function ($evt) {
			$form.find("#search").val($(this).text()).blur();
		});

		// index data
		list = that.List.map(function(e){
			e.index=[e.name, e.surname, e.band, e.why, e.age].join(" ");
			return e;
		});

		// Age range
		d.range = that.Ages = [list.min("age").age, list.max("age").age];
	},

	//UI bindings
	ui:{
		"#sort":{
			bind:"sort",
			init: function ($node) {
				//Initializing $.tags plugin
				$node.tags({tags:[["Age ↑","Name","Band","Reason"]],empty:{"Age ↓":"Age ↓"}})
			}
		},
		"#range":{
			bind:"range",
			init: function ($node, form) {
				$node.slider({
					//Initializing jQuery UI slider plugin
					range: true, min: this.Ages[0], max: this.Ages[1],
					values:this.Ages
				});
			}
		},
		"#search":{
			bind:"search",
			//conditional formatting, fills control with yellow
			css:{"my-search": /^[^\s][^\s]+/}
		},
		"#result":{
			delay:50,

			//Controls to watch
			watch:"#search,#range,#sort",

			// Function that sorts, filters and renders results,
			// returns summary string for div#result.
			bind: function (data, value, $node) {
				var that = this,
						$tbody = $node.my("find","tbody"),
						range = data.range,
						search = data.search.compact();
				//Filtering by age
				var a = this.List.filter(function(e){
					return e.age<=range[1] && e.age>=range[0]
				});
				//Applying search if any
				if (search.length) {
					var re = new RegExp(RegExp.escape(search),"i");
					a = a.filter(function(e){return re.test(e.index)});
				};
				//Sorting and rendering table
				$tbody.html(
					a.sort(this.Sorters[data.sort])
					.reduce(
						function(trail,e){
							return trail+that.Row.assign(e)
						},
						""
					)
				);
				data.result=a;

				//Compositing info line
				return a.length?"Found "
				+a.length+" early deaths, ages "+data.range.join("–")
				+(data.search?", all about <i>"+data.search+"</i>":"")
				+". It is "+(100*a.length/that.List.length).round(1)
				+"% of the list.":"No match";
			}
		}
	},

	// Sorter fuctions
	Sorters:{
		"Age ↓": function(x,y){return x.age-y.age},
		"Age ↑": function(x,y){return y.age-x.age},
		"Band":  function(x,y){
			return x.band==""?10:y.band==""?-10:x.band<y.band?-1:x.band==y.band?0:1
		},
		"Reason":function(x,y){return x.why<y.why?-1:x.why==y.why?0:1},
		"Name":  function(x,y){
			return (x.name||x.surname)<(y.name||y.surname).trim()?-1:x.name==y.name?0:1
		}
  },

	// HTML skeleton
	HTML:[
		'<h3>Rock star death stats</h3>',
		'<div class="nav">',
			'<span class="group">Sort <span id="sort"></span></span> ',
			'<span class="group">Age <span id="range"></span></span>',
			'<div class="searchgroup">',
			'<input type="text" id="search" class="ui-search" value=""/>',
			'<img src="/ico/cross-small.png" class="ui-search-clear" '
				+'onclick="$(this).siblings(\'input:eq(0)\').val(\'\').blur()"/>',
			'</div>',
		'</div>',
		'<div id="result"></div>',
		'<div id="table">',
			'<table width=700 border=0>',
				'<tbody></tbody>',
			'</table>',
		'</div>'
	],
	// Row template
	Row:'<tr><td width=200><x>{name}</x> <x>{surname}</x></td>'
		+'<td width=260><x>{band}</x></td>'
		+'<td width=50><x>{age}</x></td><td width=190><x>{why}</x></td></tr>',

	// stylesheet
	style:{
		"":"background-color:white;",
		' h3':'border-bottom: 1px solid rgba(35, 118, 200, 0.25);'
			+'margin:0 0 10px 0;padding:0 0 15px 0;',
		".nav":"padding-top:8px; height:40px; border:1px dotted #aaa; "
			+"border-width:1px 0 1px 0",
		" .nav .group ":"margin-right:10px",
		" #range":"width:150px; display:inline-block; margin-left: 15px;font-size:1em;",
		" .searchgroup":"width:150px; display:inline-block; float:right;",
		" .searchgroup input":"margin:0; width:150px; font-size:0.9em;line-height:1.2em",
		" #result":"margin:10px 0 0 0; padding-bottom:10px; "
			+"border-bottom:1px dotted #aaa;",
		" #sort":"font-size:95%;margin-left:3px;",
		" #table":{
			"":"min-height:350px;max-height:350px;overflow-y:scroll;overflow-y:overlay; "
				+"border-bottom:1px solid rgba(35, 118, 200, 0.25); overflow-x:hidden;",
			" table tr:nth-child(2n)":"background-color:#f0f5f9",
			" table td ":"padding:5px 0 6px 2px; line-height:1em;",
			" tr x ":"cursor:pointer; transition:border-bottom-color 0.3s, color 0.3s; "
				+"transition:border-bottom-color 0.3s, color 0.3s; "
				+"border-bottom:1px solid rgba(84,129,160,0);"
				+"padding-bottom:0;",
			" tr:hover x":"color:#5481A0;border-bottom:1px solid rgba(84,129,160,0.8)",
			" tr x:hover":"color:#A3293D;border-bottom-color:rgba(163,41,61,0.8)"
		},
		" .ui-search-clear":"margin: 3px 0 -3px -21px!important;"
	},
	error:"Something went wrong.<br>{message}",
	params:{delay:20}
})
