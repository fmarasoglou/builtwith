# buildwith query
## get CMS / web-server / framework info from domain


## Pending to do

- handle empty list responses
- find alternatives, this seems to work only for wordpress
- Dockerise

## Examples

```sh
curl http://localhost:5000/analyze?domain=example.com #masked response from different host
{
  "blogs": [
    "PHP",
    "WordPress"
  ],
  "cms": [
    "WordPress"
  ],
  "ecommerce": [
    "WooCommerce"
  ],
  "font-scripts": [
    "Google Font API"
  ],
  "javascript-frameworks": [
    "jQuery"
  ],
  "marketing-automation": [
    "Yoast SEO"
  ],
  "programming-languages": [
    "PHP"
  ],
  "web-frameworks": [
    "Twitter Bootstrap"
  ],
  "web-servers": [
    "Apache"
  ]
}
```