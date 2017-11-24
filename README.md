# Fact-Check
Trabalho final da disciplina de Construção de Compiladores I.

## Gramática
A gramática original e modificada utilizada está disponíveis no arquivo [gramatica.md](gramatica.md)

## Dependências
* requests==2.18.4
* nlpnet==1.2.2
* beautifulsoup4==4.6.0
* protobuf==3.5.0.post1
* React Native

## Execução

### Backend
```
cd backend/src && python3 server.py
```

### Frontend
```
cd frontend && npm i
```
Linkar dependências
```
react-native link
```
Para emular na plataforma ios
```
react-native run-ios
```
Para emular na plataforma android
```
react-native run-android
```