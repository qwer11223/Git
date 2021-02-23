const dns = require('dns')

dns.resolve('baidu.com', (err, address) => {
    if (err) {
        console.log(err)
        return
    }
    console.log(address)
})

dns.reverse('220.181.38.148', (err, domain) => {
    console.log(domain)
})