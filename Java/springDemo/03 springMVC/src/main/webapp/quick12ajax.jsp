<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<html>
<head>
    <title>Title</title>
    <script src="${pageContext.request.contextPath}/js/jquery-3.6.0.min.js"></script>
</head>
<body>
    <script>
        let userList = new Array();
        userList.push({name:'abc',age:12});
        userList.push({name:'xyz',age:23});

        $.ajax({
            type:'POST',
            url:'${pageContext.request.contextPath}/quick12',
            data:JSON.stringify(userList),
            contentType:'application/json;charset=utf-8'
        })
    </script>
</body>
</html>
