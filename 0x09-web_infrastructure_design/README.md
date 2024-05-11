# Web Infrastructure Design

This was a week-long project in which I began to research web infrastructure design. As I conducted research on different design principles, I whiteboarded diagrams of developing web infrasture. I started with a simple LAMP model and ended with a fully distributed, monitored and secured system.

Files in this project contain links to each respective whiteboard diagram.

## Tasks :page_with_curl:
*  **0. Simple web stack**
   * [0-simple_web_stack](./0-simple_web_stack): Text file containing a link to a file where I created a whiteboard of a design of a one server web infrastructure that hosts the website that is reachable via `www.foobar.com`. I started my explanation by having a user wanting to access my website. I used:
     * 1 server
     * 1 web server (Nginx)
     * 1 application server
     * 1 application file (my code base)
     * 1 database (MySQL)
     * 1 domain name `foobar.com` configured with a `www` record that points to my server IP `8.8.8.8`

*  **1. Distributed web infrastructure**
   * [1-distributed_web_infrastructure](./1-distributed_web_infrastructure1-distributed_web_infrastructure): Text file containing a link to a file where I created a design of a three web infrastructure that hosts the website `www.foobar.com`. I added:
     * 2 servers
     * 1 web server (Nginx)
     * 1 application server
     * 1 load-balancer (HAproxy)
     * 1 set of application files (my code base)
     * 1 database (MySQL)

*  **2. Secured and monitored web infrastructure**
   * [2-secured_and_monitored_web_infrastructure](./2-secured_and_monitored_web_infrastructure): Text file containing a link to a file where I created a design of a three web infrastructure that hosts the website `www.foobar.com`. It has been secured, serves encrypted traffic and is monitored. I added:
     * 3 firewalls
     * 1 SSL certificate to serve `www.foobar.com` over HTTPS
     * 3 monitoring clients (data collector for Sumologic)

*  **3. Scale up**
   * [3-scale_up](./3-scale_up): I added:
     * 1 server
     * 1 load-balancer (HAproxy) configured as cluster with the other one
     * Split components (web server, application server, database) with their own server
