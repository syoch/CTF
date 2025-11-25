pico/%.log: pico/%.py
	{ cd $(<D); python3 $(<F); cd .. ;} | tee latest.log > $@

all: $(patsubst pico/%.py,pico/%.log,$(wildcard pico/*/solve.py))

include $(wildcard pico/*/all.mk)