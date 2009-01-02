<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.1//EN"http://www.w3.org/TR/xhtml11/DTD/xhtml11.dtd">
<html>
	<head><title>comiketter</title>
		${h.stylesheet_link_tag('/comiketter.css')}
	</head>

	<body>
		<h1>comiketter</h1>
		<div id="contents">
			<div id="menu"><a href="index">search</a> | <a href="update">update</a> | <a href="help.html">help</a></div>
			<form action="updateAction" method="get">
				user: <input name="name", type="text", size="20" /><br />
				position: <input name="position", type="text", size="20" /><br />
				<input type="submit" value="regist">
			</form>
			<hr />
			% if c.error: 
				<div class="error">${c.error|h}</div> 
			% endif
			<div id="copyright">Copyrighted by showyou(showyou41 at gmail)</div>
		</div>
	</body>
</html>
