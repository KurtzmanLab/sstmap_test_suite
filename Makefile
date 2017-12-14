test_quick:
	cd tests/; python quick_test.py

test_hsa:
	cd tests/; python test_platforms_hsa.py

test_gist:
	cd tests/; python test_platforms_gist.py

test_water:
	cd tests/; python test_water_models.py

clean:
	bash clean_up.sh