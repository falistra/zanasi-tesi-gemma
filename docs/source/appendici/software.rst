Il software
===========

Acquisizione dati
~~~~~~~~~~~~~~~~~

.. code-block:: python

    # -*- coding: utf-8 -*-
    import pandas as pd
    import labels
    def getData():
        url = "https://docs.google.com/spreadsheets/d/e/2PACX-1vSe8__fQMlVJUIHbq0ZhmFRRKPciwpyn2143rwuVfQLAunZxw1JnAweUB9_j2xhPNGCDyLnZ9GOcQh6/pub?gid=0&single=true&output=csv"
        df = pd.read_csv(url)
        df = df.astype({
            "D1": pd.Int16Dtype(),
            "Flag" : '|S',
            "D1a": pd.Int16Dtype(),
            "D2a": pd.Int16Dtype(),
            "D2b": pd.Int16Dtype(),
            "D2c": pd.Int16Dtype(),
            "D3": pd.Int16Dtype(),
            "D4a": pd.Int16Dtype(),
            "D4b": pd.Int16Dtype(),
            "D4c": pd.Int16Dtype(),
            "D5": pd.Int16Dtype(),
            "D6": pd.Int16Dtype(),
            "D7": pd.Int16Dtype(),
            "D8": pd.Int16Dtype(),
            "D9": pd.Int16Dtype(),
            "D10": pd.Int16Dtype(),
            "D11": pd.Int16Dtype(),
            "D12": pd.Int16Dtype(),
            "D13": pd.Int16Dtype()
            })
        return df
    if __name__ == "__main__":
        df = getData()

Variabili e codifiche
~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

    import pandas as pd
    domande = {
        'D1':   'È la prima volta che visita il Museo Universitario Gemma?', 
        'D2a' : 'Come ne è venuto a conoscenza? (I risposta)',
        'D2b':  'Come ne è venuto a conoscenza? (II risposta)',
        'D2c':  'Come ne è venuto a conoscenza? (III risposta)',
        'D2Altro':  'Come ne è venuto a conoscenza? (Altro)',
        'D3' : 'Con chi ha visitato il Museo?',
        'D4a' : 'Per quale motivo ha visitato il Museo? (I risposta)',
        'D4b' : 'Per quale motivo ha visitato il Museo? (II risposta)',
        'D4c' : 'Per quale motivo ha visitato il Museo? (III risposta)',
        'D5' : 'Dove abita?',
        'D6':   'Sesso',
        'D7':   'Età',
        'D8' : 'Qual è il suo titolo di studio?',
        'D9' : 'Quanto tempo è durata la visita alla mostra CONFINI?',
        'D10' : 'In generale è soddisfatto della visita?',
        'D11' : 'Se ha avuto modo di seguire una visita guidata alla mostra, come si ritiene soddisfatto del percorso mostra ?',
        'D12' : 'Se ha avuto modo di seguire una visita guidata alla mostra, come si ritiene soddisfatto della visita guidata ?',
        'D13' : 'Se ha avuto modo di seguire una visita guidata alla mostra, come si ritiene soddisfatto della cortesia e competenza del personale ?',
        'D14' : 'Quale è il tema della mostra CONFINI che ha trovato di maggior interesse',
        'D15' : 'Quale è il tema parola chiave della mostra CONFINI che è rimasto più impresso',
        'D16' : 'Altre osservazioni e suggerimenti'
        }

    risposte = {
        'D1':   {1:"Sì",2:"No","All":'Totale', pd.NA:"Non risponde"},
        'D2a' : {
            1:'Da mio figlio/a, nipote',
            2: 'Da amici/parenti',
            3: 'Attraverso Internet',
            4: 'Da un pieghevole/locandina',
            5: 'Da un articolo su una rivista/giornale',
            6: 'Dalla radio/TV ',
            7: 'Casualmente, passando davanti al Museo',
            8: 'Conoscevo già il Museo',
            9: 'Altro ',
            pd.NA:"Non risponde"
            },
        'D2b' : {
            1:'Da mio figlio/a, nipote',
            2: 'Da amici/parenti',
            3: 'Attraverso Internet',
            4: 'Da un pieghevole/locandina',
            5: 'Da un articolo su una rivista/giornale',
            6: 'Dalla radio/TV ',
            7: 'Casualmente, passando davanti al Museo',
            8: 'Conoscevo già il Museo',
            9: 'Altro ',
            pd.NA:"Non risponde"
            },
        'D2c' : {
            1:'Da mio figlio/a, nipote',
            2: 'Da amici/parenti',
            3: 'Attraverso Internet',
            4: 'Da un pieghevole/locandina',
            5: 'Da un articolo su una rivista/giornale',
            6: 'Dalla radio/TV ',
            7: 'Casualmente, passando davanti al Museo',
            8: 'Conoscevo già il Museo',
            9: 'Altro ',
            pd.NA:"Non risponde"
            },
        'D3' :  {
            1: 'In gruppo organizzato',
            2: 'Da solo',
            3: 'In coppia',
            4: 'Con figli/nipoti',
            5: 'Con parenti/amici',
            pd.NA:"Non risponde"
        },
        'D4a' :  {
            1: 'Interesse specifico sulla raccolta',
            2: 'Come parte di una visita turistica nella zona/città',
            3: 'Interesse di studio/professionale',
            4: 'Per accompagnare amici/conoscenti',
            5: 'Per visitare una mostra o partecipare ad una iniziativa in corso',
            6: 'Per trascorrere del tempo libero',
            7: 'Docente di una classe in visita',
            9: 'Altro',
            pd.NA:"Non risponde"
        },
        'D4b' :  {
            1: 'Interesse specifico sulla raccolta',
            2: 'Come parte di una visita turistica nella zona/città',
            3: 'Interesse di studio/professionale',
            4: 'Per accompagnare amici/conoscenti',
            5: 'Per visitare una mostra o partecipare ad una iniziativa in corso',
            6: 'Per trascorrere del tempo libero',
            7: 'Docente di una classe in visita',
            9: 'Altro',
            pd.NA:"Non risponde"
        },
        'D4c' :  {
            1: 'Interesse specifico sulla raccolta',
            2: 'Come parte di una visita turistica nella zona/città',
            3: 'Interesse di studio/professionale',
            4: 'Per accompagnare amici/conoscenti',
            5: 'Per visitare una mostra o partecipare ad una iniziativa in corso',
            6: 'Per trascorrere del tempo libero',
            7: 'Docente di una classe in visita',
            9: 'Altro',
            pd.NA:"Non risponde"
        },
        'D5' :  {
            1:'In questa provincia',
            2:'In Italia (indicare la provincia)',
            3:'All’estero',
            pd.NA:"Non risponde"
        },
        'D6':   {
            1:"Maschio",
            2:"Femmina",
            3:"Femmina",
            "All":'Totale', 
            pd.NA:"Non risponde"
        },
        'D7':   {
            1:"Meno di 18",
            2:"Tra 18 e 30",
            3:"Tra 31 e 45",
            4:"Tra 46 e 65",
            5:"Più di 65",
            "All":'Totale',
            pd.NA:"Non risponde"
        }, 
        'D8' : {
        1: 'Elementare',
        2: 'Medie inferiori',
        3: 'Diploma medie superiori',
        4: 'Laurea o titoli post-laurea',
        5: 'Nessuno',
        pd.NA:"Non risponde"
        },
        'D9' : {
        1:'Meno di 30 minuti',
        2:'Da 30 minuti a 1 ora',
        3:'Da 1 a 2 ore',
        4:'Più di 2 ore',
        pd.NA:"Non risponde"  
        },
        'D10' : {
        1:'Per niente',
        2:'Poco',
        3:'Abbastanza',
        4:'Molto',
        pd.NA:"Non risponde"
        },
        'D11': {
        1:'Per niente',
        2:'Poco',
        3:'Abbastanza',
        4:'Molto',
        pd.NA:"Non risponde"
        },
        'D12': {
        1:'Per niente',
        2:'Poco',
        3:'Abbastanza',
        4:'Molto',
        pd.NA:"Non risponde"
        },
        'D13': {
        1:'Per niente',
        2:'Poco',
        3:'Abbastanza',
        4:'Molto',
        pd.NA:"Non risponde"
        }
    }

    risposte_short = {
        'D1':   {1:"Sì",2:"No","All":'Totale', pd.NA:"Non risponde"},
        'D2a' : {
            1:'figli',
            2: 'amici/parenti',
            3: 'Internet',
            4: 'pieghevole',
            5: 'giornale',
            6: 'radio/TV ',
            7: 'casualmente',
            8: 'conoscevo',
            9: 'altro ',
            pd.NA:"Non risponde"
            },
        'D2b' : {
            1:'Da mio figlio/a, nipote',
            2: 'Da amici/parenti',
            3: 'Attraverso Internet',
            4: 'Da un pieghevole/locandina',
            5: 'Da un articolo su una rivista/giornale',
            6: 'Dalla radio/TV ',
            7: 'Casualmente, passando davanti al Museo',
            8: 'Conoscevo già il Museo',
            9: 'Altro ',
            pd.NA:"Non risponde"
            },
        'D2c' : {
            1:'Da mio figlio/a, nipote',
            2: 'Da amici/parenti',
            3: 'Attraverso Internet',
            4: 'Da un pieghevole/locandina',
            5: 'Da un articolo su una rivista/giornale',
            6: 'Dalla radio/TV ',
            7: 'Casualmente, passando davanti al Museo',
            8: 'Conoscevo già il Museo',
            9: 'Altro ',
            pd.NA:"Non risponde"
            },
        'D3' :  {
            1: 'gruppo',
            2: 'solo',
            3: 'coppia',
            4: 'figli',
            5: 'amici',
            pd.NA:"Non risponde"
        },
        'D4a' :  {
            1: 'raccolta',
            2: 'turistica',
            3: 'studio',
            4: 'accompagnare',
            5: 'mostra',
            6: 'tempo libero',
            7: 'docente',
            9: 'altro',
            pd.NA:"Non risponde"
        },
        'D4b' :  {
            1: 'Interesse specifico sulla raccolta',
            2: 'Come parte di una visita turistica nella zona/città',
            3: 'Interesse di studio/professionale',
            4: 'Per accompagnare amici/conoscenti',
            5: 'Per visitare una mostra o partecipare ad una iniziativa in corso',
            6: 'Per trascorrere del tempo libero',
            7: 'Docente di una classe in visita',
            9: 'Altro',
            pd.NA:"Non risponde"
        },
        'D4c' :  {
            1: 'Interesse specifico sulla raccolta',
            2: 'Come parte di una visita turistica nella zona/città',
            3: 'Interesse di studio/professionale',
            4: 'Per accompagnare amici/conoscenti',
            5: 'Per visitare una mostra o partecipare ad una iniziativa in corso',
            6: 'Per trascorrere del tempo libero',
            7: 'Docente di una classe in visita',
            9: 'Altro',
            pd.NA:"Non risponde"
        },
        'D5' :  {
            1:'provincia',
            2:'Italia',
            3:'estero',
            pd.NA:"Non risponde"
        },
        'D6':   {
            1:"Maschio",
            2:"Femmina",
            "All":'Totale', 
            pd.NA:"Non risponde"
        },
        'D7':   {
            1:"Meno di 18",
            2:"Tra 18 e 30",
            3:"Tra 31 e 45",
            4:"Tra 46 e 65",
            5:"Più di 65",
            "All":'Totale',
            pd.NA:"Non risponde"
        }, 
        'D8' : {
        1: 'Elementare',
        2: 'Medie inferiori',
        3: 'Diploma medie superiori',
        4: 'Laurea o titoli post-laurea',
        5: 'Nessuno',
        pd.NA:"Non risponde"
        },
        'D9' : {
        1:'< 30mm',
        2:'30mm-1ora',
        3:'1-2ore',
        4:'+2ore',
        pd.NA:"Non risponde"  
        },
        'D10' : {
        1:'Per niente',
        2:'Poco',
        3:'Abbastanza',
        4:'Molto',
        pd.NA:"Non risponde"
        },
        'D11': {
        1:'Per niente',
        2:'Poco',
        3:'Abbastanza',
        4:'Molto',
        pd.NA:"Non risponde"
        },
        'D12': {
        1:'Per niente',
        2:'Poco',
        3:'Abbastanza',
        4:'Molto',
        pd.NA:"Non risponde"
        },
        'D13': {
        1:'Per niente',
        2:'Poco',
        3:'Abbastanza',
        4:'Molto',
        pd.NA:"Non risponde"
        }
    }



Statistiche descrittive
~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

    from etl import getData
    import pandas as pd
    import labels
    # from pretty_html_table import build_table
    import matplotlib.pyplot as plt
    def label_values(d,labels):
        return {labels[k] : v for k,v in sorted(d.items())}
    df = getData()
    tables_html = []
    for D in ['D1','D2a','D3','D4a','D5','D6','D7','D8','D9','D10','D11','D12','D13']: # ,'D3','D4a','D5','D6','D7','D8','D9','D10','D11','D12','D13']:
        data = df[D]
        data = data.apply(lambda x: labels.risposte[D][x])
        freqs = data.value_counts()
        percent100 = data.value_counts(normalize=True)
        stat = pd.DataFrame({'#': freqs, '100%': percent100})
        stat.sort_values(by=['#'], inplace=True, ascending=False)

        def ff(x):
            return ' {:<8.2%}'.format(x)
       
        img_file = f'{D}.jpg'
        table = stat.to_html(float_format=ff)
        tables_html.append(f'''
            <DIV class="testo_domanda">{labels.domande[D]}
            </DIV>
            <DIV style="float:left; display:block;">
            {table}
            </DIV>
            <DIV style="float:left;" > <IMG src='{img_file}'> </DIV>
            <div style="clear:both;"></div> 
        ''')

        plt.figure()
        freqs.loc[~freqs.index.isin(['Non risponde'])].plot.pie(y='#',textprops={'size': 'smaller'},autopct='%1.1f%%', shadow=True)
        plt.ylabel("")
        plt.savefig(f'./public/frequenze semplici/{img_file}')
        plt.close()

        with open(f'./public/frequenze semplici/Frequenze.html','w') as f:
            styles = '''
            table.dataframe > tbody > tr > th {
                text-align: left;
            }

            table.dataframe > tbody > tr > td {
                text-align: right;
            }


            .testo_domanda {
                margin-top: 20px;
                margin-bottom: 10px;
                color: blue;
                font-family: sans-serif;
                font-style: normal;
                font-variant: normal;
                font-weight: bold;
                font-size: large;
                line-height: 100%;
                word-spacing: normal;
                letter-spacing: normal;
                text-decoration: none;
                text-transform: none;
                text-align: left;
                text-indent: 0ex;
            }

            '''

            html_string = f'''
            <html>
            <head>
                <meta charset="UTF-8">
                <title>Frequenze semplici risposte</title>
                <style>
                {styles}
                </style>

            </head>
            <body>
                <div>Frequenze semplici delle risposte alle domande del questionario</div>
                <div>(Nei grafici sono escluse le mancate risposte)</div>
                <HR>
                {'<HR>'.join(tables_html)}
            </body>
            </html>
            '''
        
            f.write(html_string)

Statistiche inferenti
~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python


    from etl import getData
    import pandas as pd
    import labels
    import matplotlib.pyplot as plt

    from scipy.stats import chi2_contingency
    import seaborn as sns

    def label_values(d,labels):
        return {labels[k] : v for k,v in sorted(d.items())}

    df = getData()

    def ff(x):
        return '{}%'.format(round(x,2))

    analytics = open('./public/analytics.html','w',encoding='utf-8')
    analytics.write("""
    <meta charset="UTF-8">
    Fra le seguenti coppie di domande <B>può essere rifiutata l'ipotesi di indipendenza H0</B> <BR/>
    A favore dell'ipotesi alternativa di un legame, <BR/>
    con una probabilità  di commettere errore minore di...
    <HR>
    """)

    #for var_riga in ['D5','D6','D7','D8']:
    #    for var_col in ['D2a','D3','D4a','D9','D10','D11','D12','D13']:

    for var_riga in ['D5','D6','D7','D8','D2a','D3','D4a','D9','D10','D11','D12','D13']:
        for var_col in ['D5','D6','D7','D8','D2a','D3','D4a','D9','D10','D11','D12','D13']:
            if var_col == var_riga:
                continue

            tables_html = []

            valori_assoluti = pd.crosstab(df[var_riga], df[var_col],margins=True,margins_name='Totale')
            valori_assoluti.rename(columns=labels.risposte[var_col], index=labels.risposte[var_riga], inplace = True)
            #print(valori_assoluti)
            #print()
            table_valori_assoluti = valori_assoluti.to_html(float_format=ff)

            pct_totale = pd.crosstab(df[var_riga], df[var_col], normalize='all',margins=True, margins_name='Totale').round(4)*100
            pct_totale.rename(columns=labels.risposte[var_col], index=labels.risposte[var_riga], inplace = True)
            table_pct_totale = pct_totale.to_html(float_format=ff)

            pct_colonna = pd.crosstab(df[var_riga], df[var_col], normalize='columns',margins=True, margins_name='%% riga').round(4)*100
            pct_colonna.rename(columns=labels.risposte[var_col], index=labels.risposte[var_riga], inplace = True)
            table_pct_colonna = pct_colonna.to_html(float_format=ff)

            pct_riga = pd.crosstab(df[var_riga], df[var_col], normalize='index',margins=True, margins_name='%% colonna').round(4)*100
            pct_riga.rename(columns=labels.risposte[var_col], index=labels.risposte[var_riga], inplace = True)
            table_pct_riga = pct_riga.to_html(float_format=ff)
            
            img_file = f'{var_riga}_X_{var_col}.png'
            plt.figure(figsize=(6,4)) 
            valori_assoluti_graph = pd.crosstab(df[var_riga], df[var_col])
            valori_assoluti_graph.rename(columns=labels.risposte_short[var_col], index=labels.risposte_short[var_riga], inplace = True)
            sns.heatmap(valori_assoluti_graph, annot=True, cmap="YlGnBu")
            plt.savefig(f'./public/incroci/{img_file}')
            plt.close()

            # Chi-square test of independence. 
            c, p, dof, expected = chi2_contingency(valori_assoluti_graph)
            if p < 0.05:
                non = ''
                msg = f'''
                {p:0.2} - "{labels.domande[var_riga]} ({var_riga})" <=> "{labels.domande[var_col]} ({var_col})"
                <BR/>
                '''
                analytics.write(msg)

            else:
                non = 'non'
            giudizio = f'{non} può essere rifiutata' 
            # Print the p-value
            # print(p)

                
            tables_html.append(f'''
                Frequenze incrociate tra domande:<BR/>
                <DIV class="testo_domanda">
                "{labels.domande[var_riga]} ({var_riga})" ❌ "{labels.domande[var_col]} ({var_col})"
                </DIV>
                <div class="caption_table"> Valori assoluti </div>
                <div>{table_valori_assoluti}</DIV>
                <DIV> <IMG src="{img_file}"> </DIV>
                <div class="caption_table"> Percentuali sul totale </div>
                <div>{table_pct_totale}</DIV>
                <div class="caption_table"> Percentuali di colonna </div>
                <div>{table_pct_colonna}</DIV>
                <div class="caption_table"> Percentuali di riga </div>
                <div>{table_pct_riga}</DIV>
                <div id="chiquadro">
                Test di indipendenza 𝛘².<BR/>
                Probabilitá di ipotesi di indipendenza tra le due variabili (H0):  {p:0.2}.<BR/>
                "{labels.domande[var_riga]} ({var_riga})" ❌ "{labels.domande[var_col]} ({var_col})": <BR/>
                L'ipotesi (H0) <span id="non">{giudizio}</span>.</BR>:
                <span id="non">{non}</span> si può sostenere una legame di dipendenza fra loro.
                </div>
            ''')

            with open(f'./public/incroci/{labels.domande[var_riga]}_X_{labels.domande[var_col]}.html','w') as f:
                styles = '''
                table.dataframe > tbody > tr > th {
                    text-align: left;
                }

                table.dataframe > tbody > tr > td {
                    text-align: right;
                }

                .caption_table {
                    margin-top: 15px;
                    font-family: verdana;
                    font-weight: bold;
                }

                .testo_domanda {
                    margin-top: 20px;
                    margin-bottom: 10px;
                    color: blue;
                    font-family: sans-serif;
                    font-style: normal;
                    font-variant: normal;
                    font-weight: bold;
                    font-size: x-large;
                    line-height: 100%;
                    word-spacing: normal;
                    letter-spacing: normal;
                    text-decoration: none;
                    text-transform: none;
                    text-align: left;
                    text-indent: 0ex;
                }

                div#chiquadro {
                    width: 700px;
                    margin-top: 20px;
                    border: solid 2px red;
                    color: black;
                    font-family: verdana;
                    font-style: normal;
                    font-variant: normal;
                    font-weight: normal;
                }

                span#non {
                    color: red;
                    font-variant: large;
                }

                '''

                html_string = f'''
                <html>
                <head>
                    <meta charset="UTF-8">
                    <title>{var_riga} X {var_col} </title>
                    <style>
                    {styles}
                    </style>

                </head>
                <body>
                    {'<HR>'.join(tables_html)}
                </body>
                </html>
                '''
            
                f.write(html_string)