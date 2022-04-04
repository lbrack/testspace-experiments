# Order Maniftest

The following is an example of publishing a manifest containing information about all
the orders created. 

We could do the following:

- Save each order in the pytest.stash. At the end of a run, check the outcome of each orders and save it
  into the manifest. 
- This could include the purpose of the order, information about the order used, the design files, etc. 

## Example

- [6184](https://internal-staging.tempoautomation.com/orders/6184/details) Default pipeline with 2e2 simple
- [6183](https://internal-staging.tempoautomation.com/orders/6183/details)

## Testspace Command

```shell
⚡ ⇒  testspace push xunit-report.xml @artifact-list.txt
Aggregating content...
Uploading to Testspace (https://tempoautomation.testspace.com/projects/testspace-experiments/spaces/artifacts)...
  https://tempoautomation.testspace.com/spaces/169496/result_sets/244104
```

- [artifact-list.txt](./artifact-list.txt)
- [manifest.md](./manifest.md)