import matplotlib.pyplot as plt

# Data from the terminal output
block_sizes = [16, 64, 256, 1024, 8192, 16384]

aes_128_throughput = [1102777.38, 1436001.31, 1532286.88, 1555665.27, 1551584.30, 1554477.51]
aes_192_throughput = [995030.22, 1173974.12, 1258875.11, 1297984.39, 1280826.14, 1298012.81]
aes_256_throughput = [579671.44, 1044819.73, 1105381.46, 1115033.26, 1116990.20, 1126662.14]

# Plotting the graph
plt.figure(figsize=(10, 6))

plt.plot(block_sizes, aes_128_throughput, label='AES-128-CBC', marker='o')
plt.plot(block_sizes, aes_192_throughput, label='AES-192-CBC', marker='o')
plt.plot(block_sizes, aes_256_throughput, label='AES-256-CBC', marker='o')

plt.xlabel('Block Size (bytes)')
plt.ylabel('Throughput (KBytes/s)')
plt.title('AES Performance Comparison')
plt.legend()
plt.grid(True)

plt.savefig('aes_performance_comparison.png')

plt.show()







# RSA Data
rsa_key_sizes = [512, 1024, 2048, 3072, 4096, 7680, 15360]
rsa_sign_throughput = [53202.4, 10915.0, 1772.7, 611.2, 279.2, 34.0, 6.4]
rsa_verify_throughput = [557330.8, 225157.2, 70508.0, 33309.3, 19366.5, 5638.5, 1439.6]
rsa_encrypt_throughput = [489539.4, 209484.2, 68168.0, 32570.8, 19008.7, 5603.2, 1424.1]
rsa_decrypt_throughput = [42903.3, 10325.1, 1747.5, 607.8, 279.6, 34.0, 6.4]

# Plotting the graph
plt.figure(figsize=(10, 6))

plt.plot(rsa_key_sizes, rsa_sign_throughput, label='RSA Sign', marker='o')
plt.plot(rsa_key_sizes, rsa_verify_throughput, label='RSA Verify', marker='o')
plt.plot(rsa_key_sizes, rsa_encrypt_throughput, label='RSA Encrypt', marker='o')
plt.plot(rsa_key_sizes, rsa_decrypt_throughput, label='RSA Decrypt', marker='o')

plt.xlabel('RSA Key Size (bits)')
plt.ylabel('Throughput (operations per second)')
plt.title('RSA Performance Comparison')
plt.legend()
plt.grid(True)

plt.savefig('rsa_performance_comparison.png')

plt.show()
