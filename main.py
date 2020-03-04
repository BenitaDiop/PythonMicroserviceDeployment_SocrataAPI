from src.APIcall import get_data, get_stats

if __name__ == '__main__':
	options = get_stats()
	print('[+] Requested ', options.page_size,  ' Records From The API Per Call') 
	print('[+] Requested To Run Query ',  options.num_pages, 'x')
	print('[+] Requested To Load Data As A ', options.output, ' File Type')
	get_data(options)
