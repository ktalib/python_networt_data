import psutil
import webbrowser
import html

def get_network_details():
    # Get network I/O statistics
    net_io = psutil.net_io_counters()

    # Get network interfaces
    net_if_addrs = psutil.net_if_addrs()

    # Create an HTML file
    html_file = open("output.html", "w")

    # Write the HTML header
    html_file.write("<html><head><title>Network Details</title></head><body>")

    # Write the network details to the HTML file
    html_file.write("<h1>Network Details</h1>")
    html_file.write("<p>Bytes Sent: {}</p>".format(net_io.bytes_sent))
    html_file.write("<p>Bytes Received: {}</p>".format(net_io.bytes_recv))
    html_file.write("<p>Packets Sent: {}</p>".format(net_io.packets_sent))
    html_file.write("<p>Packets Received: {}</p>".format(net_io.packets_recv))

    # Write the network interfaces to the HTML file
    html_file.write("<h2>Network Interfaces</h2>")
    for interface_name, interface_addresses in net_if_addrs.items():
        for address in interface_addresses:
            if str(address.family) == 'AddressFamily.AF_INET':
                html_file.write("<p>Interface Name: {}, IP Address: {}</p>".format(interface_name, address.address))

    # Write the HTML footer
    html_file.write("</body></html>")

    # Close the HTML file
    html_file.close()

    # Open the HTML file in a browser
    webbrowser.open("output.html")

if __name__ == "__main__":
    get_network_details()