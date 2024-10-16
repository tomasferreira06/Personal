# Load Balancers

When a website's traffic starts getting quite large or is running an application that needs to have high availability, one web server might no longer do the job.

Load balancers provide two main features, ensuring high traffic websites can handle the load and providing a failover if a server becomes unresponsive.

When you request a website with a load balancer, the load balancer will receive your request first and then forward it to one of the multiple servers behind it.&#x20;

The load balancer uses different algorithms to help it decide which server is best to deal with the request. A couple of examples of these algorithms are <mark style="color:yellow;">**round-robin**</mark>, which sends it to each server in turn, or <mark style="color:yellow;">**weighted**</mark>, which checks how many requests a server is currently dealing with and sends it to the least busy server.

Load balancers also perform periodic checks with each server to ensure they are running correctly; this is called a <mark style="color:yellow;">**health check**</mark>. If a server doesn't respond appropriately or doesn't respond, the load balancer will stop sending traffic until it responds appropriately again.

<figure><img src="../../../../.gitbook/assets/Capture (34).PNG" alt=""><figcaption></figcaption></figure>

