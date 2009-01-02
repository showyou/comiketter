<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.1//EN" "http://www.w3.org/TR/xhtml11/DTD/xhtml11.dtd">
<html>
	<head><title>comiketter</title>
		${h.stylesheet_link_tag('/comiketter.css')}
	</head>
	<body>
		<h1>comiketter</h1>
		<div id="contents">
			<div id="menu"><a href="index">search</a> | <a href="update">update</a> | <a href="help.html">help</a></div>

			<form action="search" method="get">
				user: <input name="name", type="text", size="20" /><br />
				<input type="submit" value="search!">
			</form>
			% if c.error:
				<div>search results:${c.error|h}</div>
			% endif
			% for message in c.messages:
				<div class="message"><span id="uname">${message.name |h}</span> : <span id="upos">${message.pos|h}</span> <span id="update">at ${message.update}</span></div>
			% endfor

			<hr />
			<div id="copyright">Copyright 2008 showyou(showyou41 at gmail)</div>
		</div>

	</body>
</html>
