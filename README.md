# nft-gift-button-frontend

Currently, there is a Django as html/static server only. 
Thus, no interaction with the Django backend as it often happens.
To note, all frontend logic is **inside client html** file 
and itself it consists of **pure frontend  html** that will migrate to reactApp in the future, i.e. in the second milestone accroding to grant roadmap. 

## Start
Prepare `.env` according to [.env.example](.env.example) (coz we want to aware frontend what backend it should use) and
```
docker-compose up
```

## Demonstration Flow

### Send NFT 
1. Go to http://localhost:8015/send
2. Login with metamask
3. Complete steps

### Receive NFT
1. Go to http://localhost:8015/receive
2. Relogin as a receiver
3. Complete steps
