class WSHandler(WebSocketHandler):
  orgs = conf.orgs

  def open(self):
    print("WebSocket opened")
    self.write_message("connection opened")

    def send_response(x):
        self.write_message(json.dumps(x))

    def on_error(ex):
        print(ex)

    self.subject = Subject()

    user_input = self.subject.throttle_last(
        1000  # Given the last value in a given time interval
    ).start_with(
        ''  # Immediately after the subscription sends the default value
    ).filter(
        lambda text: not text or len(text) > 2
    )

    interval_obs = Observable.interval(
        60000  #refresh the value every 60 Seconds for periodic updates
    ).start_with(0)

    self.combine_latest_sbs = user_input.combine_latest(
        interval_obs, lambda input_val, i: input_val
    ).do_action(
        lambda x: send_response('clear')
    ).flat_map(
        self.get_data
    ).subscribe(send_response, on_error)

  def get_data(self,query):
    """ query the data to the API and return the contet filtered"""
    return Observable.from_list(
        self.orgs
    ).flat_map(
        lambda name: Observable.from_future(self.get_org_repos(name))
    ).flat_map(
        lambda x: Observable.from_list(

            self.get_info(x) #transform the response to a json list

         ).filter(

            lambda val: (val.get("description") is not None
        and (val.get("description").lower()).find(query.lower())!= -1)
                or (val.get("language") is not None
                and (val.get("language").lower()).find(query.lower())!= -1)
         ).take(10)  #just take 10 repos from each org

    ).map(lambda x: {'name': x.get("name"),
    'stars': str(x.get("stargazers_count")),
    'link': x.get("svn_url"),'description': x.get("description"),
    'language': x.get("language")})

