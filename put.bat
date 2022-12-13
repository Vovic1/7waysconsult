rem curl -H "Accept: application/json" -H "Content-type: application/json" -X PUT -d '{"id":"1", "name":"petr", "descr":"apostol", "is_act":"1", "is_del":"0"}' http://localhost:8080/poll/3

curl -X PUT -d '{"id":"3", "name":"petr", "descr":"apostol", "is_act":"1", "is_del":"0" }' -H "Content-Type: application/json" http://localhost:8080/poll/3