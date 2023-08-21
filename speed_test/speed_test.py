import speedtest
import rich

def test():
    # using rich print to print the output in a nice way
    rich.print("[bold green]Starting speed test...[/bold green]")
    st = speedtest.Speedtest()
    # Find the best server
    rich.print("[bold green]Finding best server...[/bold green]")
    st.get_best_server()
    # ping value and print it
    ping = st.results.ping
    rich.print(f"[bold green]Ping: {ping} ms[/bold green]")
    # download speed and trak the proces and print it
    download = st.download()
    rich.print(f"[bold green]Download Speed: {download / 1024 / 1024:.2f} MB/s[/bold green]")
    # upload speed and print it
    upload = st.upload()
    rich.print(f"[bold green]Upload Speed: {upload / 1024 / 1024:.2f} MB/s[/bold green]")
    
if __name__ == "__main__":
    test()
    