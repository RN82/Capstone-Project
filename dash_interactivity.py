  dcc.Dropdown(id='site-dropdown',
                options=[
                    {'label': 'All Sites', 'value': 'ALL'},
                    {'label': 'CCAFS LC-40', 'value': 'site1'},
                    {'label': 'CCAFS SLC-40', 'value': 'site2'}
                    {'label': 'KSC LC-39A', 'value': 'site3'}
                    {'label': 'VAFB SLC-4E', 'value': 'site4'}
                ],
                value='ALL',
                placeholder="Select a Launch Site here",
                searchable=True
                ),
# Run the app
if __name__ == '__main__':
    app.run_server()