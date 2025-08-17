def gg(vipfollower,vippost,winnertakesitall):
	while True:
		try:
			
			resolution=f"{random.randint(200,2000)}x{random.randint(200,2000)}"
			user_agent=f"Instagram 311.0.0.32.118 Android (random.choice(['23/6.0','24/7.0','25/7.1.1','26/8.0','27/8.1','28/9.0']); str(random.randint(100,1300))dpi; {resolution}; random.choice(['SAMSUNG','HUAWEI','LGE/lge','HTC','ASUS','ZTE','ONEPLUS','XIAOMI','OPPO','VIVO','SONY','REALME']); SM-Tstr(random.randint(150,999)); SM-Tstr(random.randint(150,999)); qcom; en_US; 545986str(random.randint(111,999)))"
			lsd_token=''.join(random.choices(string.ascii_letters+string.digits,k=32))
			headers={'accept':'*/*','accept-language':'en,en-US;q=0.9','content-type':'application/x-www-form-urlencoded','dnt':'1','origin':'https://www.instagram.com','priority':'u=1, i','referer':'https://www.instagram.com/cristiano/following/','user-agent':user_agent,'x-fb-friendly-name':'PolarisUserHoverCardContentV2Query','x-fb-lsd':lsd_token}
			user_id=winnertakesitall()
			data={'lsd':lsd_token,'fb_api_caller_class':'RelayModern','fb_api_req_friendly_name':'PolarisUserHoverCardContentV2Query','variables':json.dumps({'userID':user_id,'username':'cristiano'}),'server_timestamps':'true','doc_id':'7717269488336001'}
			response=requests.post('https://www.instagram.com/api/graphql',headers=headers,data=data)
			user_info=response.json().get('data',{}).get('user',{})
			username=user_info.get('username','')
			infoinsta[username]=user_info
			followers=int(user_info.get('follower_count',0))
			posts=int(user_info.get('media_count',0))
			if username and followers>=vipfollower or posts>=vippost:
				dvmbmail=f"{username}@gmail.com"
				check(dvmbmail)
		except:pass

for _ in range(threds):
	Thread(target=gg,args=(vipfollower,vippost,pybasics)).start()
