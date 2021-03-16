clean:
	rm docs/* -rf

build: clean
	bundle exec jekyll build
	mv _site/* docs/

deploy: build
	git add -A
	git commit -m "Deploy"
	git checkout --orphan temp_branch
	git add -A
	git commit -m "Deploy"
	git push origin temp_branch:master --force
	git fetch --prune
	git checkout master
	git branch -D temp_branch

