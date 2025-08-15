for _ in range(threds):
	Thread(target=gg,args=(vipfollower,vippost,generate_user_id)).start()
