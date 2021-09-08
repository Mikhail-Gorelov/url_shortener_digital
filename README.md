#### Task

  You need to implement a web-application that is analogous to bit.ly and similar systems.
  That is, for long urls creates their short counterparts.

  The application contains one page on which:
  A form where you can enter the URL to be shortened.
  A table with all the shortened URLs (with pagination) of a given user

#### Requirements:

  1. Application does NOT contain authorization
  2. Application tracks users by session (use Django sessions) i.e. each user has his own set of redirects (rules)
  3. The data is stored in MySQL
  4. When accessing a compressed URL, the application redirects (server-side redirect) to the appropriate URL (which is compressed)
  5. The user can optionally specify their subpart. If there is already an subpart in use, user should be informed.
  6. Django implementation
  7. Caching of redirects in redis. Need to save the shortened url mapping to the redirect with the full address, not the redirect rule object in its entirety. DO NOT USE view caching, QuerySets, or any other high-level methods which just involve setting a couple of attributes in the application configuration
  8. Cleaning old rules on a schedule
  9. deleting entries from MySQL; 
  10. purging redirects from Redis can be implemented either together with MySQL purging or by TTL

#### How to use:

  1. copy project: git clone https://github.com/Mikhail-Gorelov/url_shortener_digital.git ./project_name
  
  2. docker-compose up -d --build
  
  3. docker-compose logs -f


