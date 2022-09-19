Domande
=======

La tabella seguente contiene la liste delle coppie codice-testo delle domande.

.. list-table:: Domande e risposte
   :widths: 15 85
   :header-rows: 1

   * - Codice 
     - Testo 
   * - D1
     - È la prima volta che visita il Museo Universitario Gemma?
   * - D2
     - Come ne è venuto a conoscenza?
   * - D3
     - Con chi ha visitato il Museo?
   * - D4
     - Per quale motivo ha visitato il Museo?
   * - D5
     - Dove abita?
   * - D6
     - Sesso
   * - D7
     - Età
   * - D8
     - Qual è il suo titolo di studio?
   * - D9
     - Quanto tempo è durata la visita alla mostra CONFINI?
   * - D10
     - In generale è soddisfatto della visita?
   * - D11
     - Come si ritiene soddisfatto del percorso mostra ?
   * - D12
     - Come si ritiene soddisfatto della visita guidata 
   * - D13
     - Come si ritiene soddisfatto della cortesia e competenza del personale ?
   * - D14
     - Quale è il tema della mostra CONFINI che ha trovato di maggior interesse
   * - D15
     - Quale è il tema parola chiave della mostra CONFINI che è rimasto più impresso
   * - D16
     - Altre osservazioni e suggerimenti

La tabella seguente mostra la relazione tra (il codice del)le domande e 
la codifica delle risposte.


.. code-block:: python

    risposte = {
    'D1':   {
        1:"Sì",
        2:"No",
        pd.NA:"Non risponde"
    },
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

