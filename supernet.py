from netaddr import IPNetwork
import argparse
from pprint import pprint

def main():

    # Supercalc
    parser = argparse.ArgumentParser(description='Supernet')
    # First argument is the from IP
    parser.add_argument('from_ip', help='Starting IP Address')
    # Second argument is the end IP
    parser.add_argument('to_ip', help='Ending IP Address')

    # Parse the arguments
    args = parser.parse_args()

    # Create the IPNetwork object
    from_ip = IPNetwork(args.from_ip)
    to_ip = IPNetwork(args.to_ip)


    # Print the from and to IPs
    print('From IP: %s' % from_ip)
    print('To IP: %s' % to_ip)

    print('-------')
    # Get Supernets
    from_supernets = from_ip.supernet()
    from_supernets.append(from_ip)

    to_supernets = to_ip.supernet()
    to_supernets.append(to_ip)

    matching_supernets = list()

    # Get the matching supernets
    for from_supernet in from_supernets:
        for to_supernet in to_supernets:
            if from_supernet == to_supernet:
                matching_supernets.append(from_supernet)
                break
    
    # Print the supernet with highest prefix number
    print("Matching Supernet: %s" % matching_supernets[-1])

    # Print Host address of the supernet
    print("Host address: %s" % matching_supernets[-1].network)
    # Print Network address of the supernet
    print("Network address: %s" % matching_supernets[-1].network)
    # Print Broadcast address of the supernet
    if from_ip == to_ip:
        print("Both IPs are the same")
    else:
        print("Broadcast address: %s" % matching_supernets[-1].broadcast)
        # Print Netmask
        print("Netmask: %s" % matching_supernets[-1].netmask)
        # Print Number of hosts
        print("Number of hosts: %s" % matching_supernets[-1].size)
        # Print Number of usable hosts
        print("Number of usable hosts: %s" % (matching_supernets[-1].size - 2))
        # Print usable range
        print("Usable range: %s - %s" % (matching_supernets[-1].network + 1, matching_supernets[-1].broadcast - 1))


if __name__=='__main__':
    main()