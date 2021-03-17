from invoke import task


@task
def lint(c):
    c.run("python -m flake8 .", pty=True)
    c.run("python -m black --check .", pty=True)
