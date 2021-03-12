.PHONY: clean
clean: 
	@echo ---------------------
	@echo Running target $@
	@echo ---------------------
	@bin/clean.sh

.PHONY: index
index: clean
	@echo ---------------------
	@echo Running target $@
	@echo ---------------------
	@bin/run.sh -i