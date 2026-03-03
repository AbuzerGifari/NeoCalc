import sympy as sp
from rich.console import Console
from rich.panel import Panel
from rich.table import Table

console = Console()

class NeoCalc:
    def __init__(self):
        self.history = []

    def evaluate(self, expression):
        try:
            # Parse the string into a SymPy object
            expr = sp.sympify(expression)
            
            # Simplify and solve
            result = sp.simplify(expr)
            
            # If it's an equation (contains symbols), let's try to solve for x
            symbols = expr.free_symbols
            solution = None
            if symbols:
                solution = sp.solve(expr, list(symbols)[0])

            return result, solution
        except Exception as e:
            return None, str(e)

    def display_ui(self):
        console.print(Panel("[bold cyan]NeoCalc v1.0[/bold cyan] - Open Source Symbolic Engine", expand=False))
        
        while True:
            user_input = console.input("[bold green]math » [/bold green]")
            
            if user_input.lower() in ['exit', 'quit']:
                break
                
            res, sol = self.evaluate(user_input)
            
            if res is not None:
                table = Table(show_header=False, border_style="magenta")
                table.add_row("Result", str(res))
                if sol:
                    table.add_row("Solutions", str(sol))
                console.print(table)
            else:
                console.print(f"[bold red]Error:[/bold red] {sol}")

if __name__ == "__main__":
    calc = NeoCalc()
    calc.display_ui()
Commit at 2024-01-02T10:26:59.681959
Commit at 2024-01-25T18:17:55.847236
Commit at 2024-01-27T11:00:50.958357
Commit at 2024-01-31T07:27:48.070825
Commit at 2024-01-19T01:49:22.185208
Commit at 2024-01-16T14:43:04.295353
Commit at 2024-01-20T07:00:18.406372
Commit at 2024-01-10T12:44:45.516304
Commit at 2024-02-03T06:08:26.628746
Commit at 2024-01-18T04:58:06.742508
Commit at 2024-01-19T21:22:10.853823
Commit at 2023-12-28T16:57:19.967172
Commit at 2024-01-09T13:03:01.077784
Commit at 2024-01-16T09:24:21.189868
Commit at 2024-01-01T12:08:32.303563
Commit at 2024-01-14T11:31:51.415392
Commit at 2024-01-22T01:19:05.525513
Commit at 2024-01-12T19:30:52.634226
Commit at 2024-01-18T22:07:08.745548
Commit at 2024-01-04T17:41:11.858398
Commit at 2024-01-26T14:05:39.968382
Commit at 2024-01-04T03:44:05.080178
Commit at 2023-12-28T13:26:55.193132
Commit at 2024-02-05T11:10:24.306406
Commit at 2023-12-30T08:36:55.418024
Commit at 2024-01-30T02:59:09.528989
Commit at 2024-02-04T15:12:30.640529
Commit at 2024-01-12T15:35:15.752064
Commit at 2024-01-26T13:15:43.865641
Commit at 2024-01-07T04:44:28.975430
Commit at 2024-01-31T16:55:32.085542
Commit at 2024-01-04T14:42:29.189278
Commit at 2024-01-15T03:06:15.301562
Commit at 2024-01-28T03:33:43.416465
Commit at 2024-01-04T00:52:39.528932
Commit at 2024-01-17T14:51:06.641160
Commit at 2024-01-27T14:35:28.754512
Commit at 2024-01-12T09:50:46.865954
Commit at 2024-01-27T18:35:42.976979
Commit at 2024-01-17T18:00:49.087233
Commit at 2023-12-29T05:26:41.202290
Commit at 2024-02-02T21:59:03.312740
Commit at 2024-02-03T15:47:01.426999
Commit at 2024-01-05T06:30:46.536032
Commit at 2024-01-28T20:28:48.651229
Commit at 2024-01-23T12:51:23.759632
Commit at 2024-01-29T00:26:39.881591
Commit at 2024-01-31T00:10:00.993765
Commit at 2024-01-18T07:17:41.104458
Commit at 2024-01-09T07:51:19.216492
