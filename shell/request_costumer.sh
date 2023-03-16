#1. Set execute permission on your script using chmod command
# chmod +x script-name-here.sh
#
#2. To run your script:
# ./script-name-here.sh
#
#3. To only run:
# sh script-name-here.sh
if [ "$1" = 1 ]; then

    json_data='{"name": "Tomás Kaique Assunção", 
    "cpf": "942.554.492-10", 
    "birth_date": "27/01/2002", 
    "address": "Quadra 12 Conjunto F, 311"}'

    curl -iX POST http://127.0.0.1:8080/costumers/ \
    -H "Content-Type: application/json" \
    -d "$json_data"

elif [ "$1" = 2 ]; then
    
    curl -iX GET "http://127.0.0.1:8080/costumers/1"
    
else
    echo ">> INFORME UMA DAS OPÇÕES 1:POST, 2:GET <<"
fi