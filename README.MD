# Consumindo Betfair Sportsbook API com Django

### O objetivo desse projeto é consumir uma API que oferece placares de jogos em tempo real com o valor das odd's na casa de apostas [Betfair](https://www.betfair.com/br). Para realizar as requisições, utilizei a biblioteca [requests](https://pypi.org/project/requests/) do Python juntamente com o framework [Django](https://www.djangoproject.com/).

### Pretendo lançar em breve uma atualização, transformando essa página em uma SPA com Django (sim, isso é possível). No momento, não é nada profissional, onde eu apenas tentei consumir uma API com o Django, algo que é super comum quando pensamos em React ou em qualquer outra biblioteca queridinha dos amantes de Js. 

### Acesso a API: https://betfair-sportsbook.p.rapidapi.com/live-matches-by-sport

## Como rodar o projeto localmente?
 - Clone o repositório do projeto

        git clone https://github.com/FelZito/consumer-betfairsportsbookapi-dj.git

 - Instale as bibliotecas necessárias

        pip install -r requirements.txt

 - Seja feliz

        python manage.py runserver
