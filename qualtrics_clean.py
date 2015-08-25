exclude_columns = ["arizona_Q1A1",
"arizona_Q2A1_ggr",
"arizona_Q4A1",
"arizona_Q2A1",
"arizona_Q5A1",
"arizona_Q3A1",
"arizona_Q1A2",
"arizona_Q4A2",
"arizona_Q2A2",
"arizona_Q5A2",
"arizona_Q3A2",
"arizona_Q2A2_ggr",
"arizona_Q2A1_mfg",
"arizona_Q2A2_mfg",
"california_Q1A1",
"california_Q4A1",
"california_Q2A1",
"california_Q5A1",
"california_Q3A1",
"colorado_Q1A1",
"colorado_Q2A1_ggr",
"colorado_Q4A1",
"colorado_Q2A1",
"colorado_Q5A1",
"colorado_Q3A1",
"colorado_Q1A2",
"colorado_Q4A2",
"colorado_Q2A2",
"colorado_Q5A2",
"colorado_Q3A2",
"colorado_Q2A2_ggr",
"colorado_Q2A1_mfg",
"colorado_Q2A2_mfg",
"idaho_Q1A1",
"idaho_Q2A1_ggr",
"idaho_Q4A1",
"idaho_Q2A1",
"idaho_Q5A1",
"idaho_Q3A1",
"idaho_Q1A2",
"idaho_Q4A2",
"idaho_Q2A2",
"idaho_Q5A2",
"idaho_Q3A2",
"idaho_Q2A2_ggr",
"idaho_Q2A1_mfg",
"idaho_Q2A2_mfg",
"montana_Q1A1",
"montana_Q2A1_ggr",
"montana_Q4A1",
"montana_Q2A1",
"montana_Q5A1",
"montana_Q3A1",
"montana_Q1A2",
"montana_Q4A2",
"montana_Q2A2",
"montana_Q5A2",
"montana_Q3A2",
"montana_Q2A2_ggr",
"montana_Q2A1_mfg",
"montana_Q2A2_mfg",
"nevada_Q1A1",
"nevada_Q2A1_ggr",
"nevada_Q4A1",
"nevada_Q2A1",
"nevada_Q5A1",
"nevada_Q3A1",
"nevada_Q1A2",
"nevada_Q4A2",
"nevada_Q2A2",
"nevada_Q5A2",
"nevada_Q3A2",
"nevada_Q2A2_ggr",
"nevada_Q2A1_mfg",
"nevada_Q2A2_mfg",
"new mexico_Q1A1",
"new mexico_Q2A1_ggr",
"new mexico_Q4A1",
"new mexico_Q2A1",
"new mexico_Q5A1",
"new mexico_Q3A1",
"new mexico_Q1A2",
"new mexico_Q4A2",
"new mexico_Q2A2",
"new mexico_Q5A2",
"new mexico_Q3A2",
"new mexico_Q2A2_ggr",
"new mexico_Q2A1_mfg",
"new mexico_Q2A2_mfg",
"oregon_Q1A1",
"oregon_Q2A1_ggr",
"oregon_Q4A1",
"oregon_Q2A1",
"oregon_Q5A1",
"oregon_Q3A1",
"oregon_Q1A2",
"oregon_Q4A2",
"oregon_Q2A2",
"oregon_Q5A2",
"oregon_Q3A2",
"oregon_Q2A2_ggr",
"oregon_Q2A1_mfg",
"oregon_Q2A2_mfg",
"texas_Q1A1",
"texas_Q2A1_ggr",
"texas_Q4A1",
"texas_Q2A1",
"texas_Q5A1",
"texas_Q3A1",
"texas_Q1A2",
"texas_Q4A2",
"texas_Q2A2",
"texas_Q5A2",
"texas_Q3A2",
"texas_Q2A2_ggr",
"texas_Q2A1_mfg",
"texas_Q2A2_mfg",
"utah_Q1A1",
"utah_Q2A1_ggr",
"utah_Q4A1",
"utah_Q2A1",
"utah_Q5A1",
"utah_Q3A1",
"utah_Q1A2",
"utah_Q4A2",
"utah_Q2A2",
"utah_Q5A2",
"utah_Q3A2",
"utah_Q2A2_ggr",
"utah_Q2A1_mfg",
"utah_Q2A2_mfg",
"washington_Q1A1",
"washington_Q2A1_ggr",
"washington_Q4A1",
"washington_Q2A1",
"washington_Q5A1",
"washington_Q3A1",
"washington_Q1A2",
"washington_Q4A2",
"washington_Q2A2",
"washington_Q5A2",
"washington_Q3A2",
"washington_Q2A2_ggr",
"washington_Q2A1_mfg",
"washington_Q2A2_mfg",
"wyoming_Q1A1",
"wyoming_Q2A1_ggr",
"wyoming_Q4A1",
"wyoming_Q2A1",
"wyoming_Q5A1",
"wyoming_Q3A1",
"wyoming_Q1A2",
"wyoming_Q4A2",
"wyoming_Q2A2",
"wyoming_Q5A2",
"wyoming_Q3A2",
"wyoming_Q2A2_ggr",
"wyoming_Q2A1_mfg",
"wyoming_Q2A2_mfg",
"california_Q2A1_ggr",
"california_Q1A2",
"california_Q4A2",
"california_Q2A2",
"california_Q5A2",
"california_Q3A2",
"california_Q2A2_ggr",
"california_Q2A1_mfg",
"california_Q2A2_mfg",
"arizona",
"california",
"new.mexico",
"texas",
"washington",
"wyoming",
"oregon",
"montana",
"nevada",
"idaho",
"utah",
"colorado",
"END"]



questions = ['Current $ Personal Income',
			'Retail Sales',
			'Wage & Salary Employment',
			'Population Growth',
			'Single-family Housing Permits',
			'Gross Gaming Revenue',
			'Manufacturing Employment']

column_rename = {'Current $ Personal Income':'Q1',
				'Retail Sales':'Q2',
				'Wage & Salary Employment':'Q3',
				'Population Growth':'Q4',
				'Single-family Housing Permits':'Q5',
				'Gross Gaming Revenue':'Q2_ggr',
				'Manufacturing Employment':'Q2_mfg'}

final_column_rename = {'Q2_ggrA1':'Q2A1_ggr',
						'Q2_ggrA2':'Q2A2_ggr',
						'Q2_mfgA1':'Q2A1_mfg',
						'Q2_mfgA2':'Q2A2_mfg'}

master_column_names = ['Q1A1',
						'Q1A2',
						'Q2A1',
						'Q2A2',
						'Q3A1',
						'Q3A2',
						'Q4A1',
						'Q4A2',
						'Q5A1',
						'Q5A2',
						'Q2A1_mfg',
						'Q2A2_mfg',
						'Q2A1_ggr',
						'Q2A2_ggr']

